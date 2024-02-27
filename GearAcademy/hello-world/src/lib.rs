#![no_std]
use gstd::{debug, errors::Result as GstdResult, msg, prelude::*};
use hello_world_io::InputMessages;

static mut GREETING: Option<String> = None;

#[no_mangle]
extern "C" fn init() {
    let greeting: String = msg::load().expect("Can't load init message");
    debug!("Program was initialized with message {:?}", greeting);
    unsafe { GREETING = Some(greeting) };
}

#[no_mangle]
extern "C" fn handle() {
    let input_message: InputMessages = msg::load().expect("Error in loading InputMessages");
    let greeting = unsafe { GREETING.as_mut().expect("The contract isn't initialized") };
    match input_message {
        InputMessages::SendHelloTo(account) => {
            debug!("Message: SendHelloTo {:?}", account.as_ref());
            msg::send(account, greeting, 0).expect("Error in sending Hello message to account");
        }
        InputMessages::SendHelloReply => {
            debug!("Message: SendHelloReply");
            msg::reply(greeting, 0).expect("Error in sending reply");
        }
    }
}

#[no_mangle]
extern "C" fn state() {
    let greeting = unsafe { GREETING.as_ref().expect("The contract isn't initialized") };
    msg::reply(greeting, 0).expect("Failed to share state");
}
