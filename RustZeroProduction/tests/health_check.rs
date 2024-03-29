use std::net::TcpListener;

#[tokio::test]
async fn health_check_works() {
    /* properties of `health_check` covered
     * - is exposed at `/health_check`
     * - is behind a `GET` method
     * - always returns a 200
     * - its response has no body
     * */
    // setup
    let address = spawn_app();
    let client = reqwest::Client::new();
    // action
    let response = client
        .get(&format!("{}/health_check", &address))
        .send()
        .await
        .expect("Failed to execute request.");
    assert!(response.status().is_success());
    assert_eq!(Some(0), response.content_length());
}

fn spawn_app() -> String {
    let listener = TcpListener::bind("127.0.0.1:0").expect("Failed to bind random port");
    // retrive the port assigned by the OS
    let port = listener.local_addr().unwrap().port();
    let server = newsletter::run(listener).expect("Failed to bind address");
    let _ = tokio::spawn(server);
    format!("http://127.0.0.1:{}", port)
}
