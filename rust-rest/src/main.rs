use actix_web::{get, web, HttpResponse, Result};
use serde::{Deserialize, Serialize};
use num_bigint::BigUint;

#[derive(Serialize, Deserialize)]
struct FibonacciResponse {
    value: BigUint,
}

#[derive(Serialize, Deserialize)]
struct Document<T> {
    data: T,
}

#[derive(Serialize, Deserialize)]
struct FibonacciRequest {
    order: usize,
}

#[get("/fibonacci/v1/sequence/{order}")]
async fn index(param: web::Path<FibonacciRequest>) -> Result<HttpResponse> {
    let order = param.order;
    let mut f: Vec<BigUint> = Vec::new();
    f.push(0);
    f.push(1);
    for i in 2..(order + 1) {
        f.push(f[(i - 1) as BigUint] + f[(i - 2) as BigUint]);
    }
    Ok(HttpResponse::Ok().json(Document {
        data: FibonacciResponse {
            value: f[order as BigUint],
        },
    }))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    use actix_web::{App, HttpServer};

    HttpServer::new(|| App::new().service(index))
        .bind(("0.0.0.0", 8080))?
        .run()
        .await
}
