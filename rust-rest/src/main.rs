use actix_web::{get, web, HttpResponse, Result};
use serde::{Deserialize, Serialize};

#[derive(Serialize)]
struct Measurement {
    temperature: f32,
}

#[get("/temperature")]
async fn current_temperature() -> impl Responder {
    web::Json(Measurement { temperature: 42.3 })
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    use actix_web::{App, HttpServer};

    HttpServer::new(|| App::new().service(current_temperature))
        .bind("127.0.0.1:8080")?
        .run()
        .await
}