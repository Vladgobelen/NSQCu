use crate::config;
use crate::modules::addon_manager;
use egui::{CentralPanel, ProgressBar, ScrollArea};
use log::{error, info};
use reqwest::blocking::Client;
use serde::Deserialize;
use std::sync::{Arc, Mutex};

#[derive(Debug, Clone, Deserialize)]
pub struct Addon {
    pub name: String,
    pub link: String,
    pub description: String,
    #[serde(rename = "type")]
    pub addon_type: u8,
    pub source_path: String,
    pub target_path: String,
}

#[derive(Default)]
pub struct AddonState {
    pub target_state: Option<bool>,
    pub installing: bool,
    pub progress: f32,
}

pub struct App {
    pub addons: Vec<(Addon, Arc<Mutex<AddonState>>)>,
    pub client: Client,
}

impl App {
    pub fn new(cc: &eframe::CreationContext<'_>) -> Self {
        cc.egui_ctx.set_visuals(egui::Visuals::dark());
        
        config::check_game_directory().unwrap_or_else(|e| {
            error!("{}", e);
            panic!("{}", e);
        });

        let client = Client::new();
        let addons = config::load_addons_config_blocking(&client)
            .expect("Failed to load addons config");

        let addons_with_state = addons.into_iter().map(|(name, addon)| {
            let installed = addon_manager::check_addon_installed(&addon);
            info!("Addon '{}' installed: {}", name, installed);
            (
                addon,
                Arc::new(Mutex::new(AddonState {
                    target_state: Some(installed),
                    installing: false,
                    progress: 0.0,
                }))
            )
        }).collect();

        Self { addons: addons_with_state, client }
    }

    fn toggle_addon(&mut self, index: usize) {
        let (addon, state) = self.addons[index].clone();
        let mut state_lock = state.lock().unwrap();
        
        if state_lock.installing {
            return;
        }
        
        let current_actual_state = addon_manager::check_addon_installed(&addon);
        let desired_state = !current_actual_state;
        
        state_lock.target_state = Some(desired_state);
        state_lock.installing = true;
        state_lock.progress = 0.0;
        drop(state_lock);

        let client = self.client.clone();
        std::thread::spawn(move || {
            info!("Starting operation for: {}", addon.name);
            
            let result = if desired_state {
                addon_manager::install_addon(&client, &addon, state.clone())
            } else {
                addon_manager::uninstall_addon(&addon)
            };

            let mut state = state.lock().unwrap();
            match result {
                Ok(success) => {
                    state.target_state = Some(success == desired_state);
                    info!("Operation status: {}", success);
                },
                Err(e) => {
                    error!("Operation failed: {:?}", e);
                    state.target_state = Some(current_actual_state);
                }
            }
            state.installing = false;
        });
    }
}

impl eframe::App for App {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        CentralPanel::default().show(ctx, |ui| {
            ui.heading("Менеджер аддонов Ночной Стражи");
            ui.separator();

            let mut indices_to_toggle = Vec::new();

            ScrollArea::vertical().show(ui, |ui| {
                for (i, (addon, state)) in self.addons.iter().enumerate() {
                    let state = state.lock().unwrap();
                    let current_state = state.target_state.unwrap_or_else(|| 
                        addon_manager::check_addon_installed(&addon)
                    );
                    
                    ui.horizontal(|ui| {
                        let response = ui.add_enabled_ui(!state.installing, |ui| {
                            ui.checkbox(&mut current_state.clone(), "")
                        });

                        if response.inner.changed() {
                            indices_to_toggle.push(i);
                        }

                        ui.vertical(|ui| {
                            ui.heading(&addon.name);
                            ui.label(&addon.description);
                            if state.installing {
                                ui.add(ProgressBar::new(state.progress).show_percentage());
                            }
                        });
                    });
                    ui.separator();
                }
            });

            for index in indices_to_toggle {
                self.toggle_addon(index);
            }
        });

        ctx.request_repaint();
    }
}
