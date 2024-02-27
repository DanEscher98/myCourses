use gtest::{Log, Program, System};
use hello_world::InputMessages;

#[test]
fn hello_test() {
    let sys = System::new();
    sys.init_logger();
    let program = Program::current(&sys);
    let msg = "Hello World";
    let res = program.send(2, String::from(msg));
    assert!(!res.main_failed());

    let hello_recipient: u64 = 4;
    let res = program.send(2, InputMessages::SendHelloTo(hello_recipient.into()));

    let expected_log = Log::builder()
        .dest(hello_recipient)
        .payload(String::from(msg));
    assert!(res.contains(&expected_log));
}
