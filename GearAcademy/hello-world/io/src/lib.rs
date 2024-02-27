#![no_std]
use gmeta::{In, InOut, Metadata, Out};
use gstd::{prelude::*, ActorId};

pub struct ProgramMetadata;

impl Metadata for ProgramMetadata {
    type Init = In<String>;
    type Handle = InOut<InputMessages, String>;
    type Reply = ();
    type Others = ();
    type Signal = ();
    type State = Out<String>;
}

#[derive(Debug, Encode, Decode, TypeInfo)]
pub enum InputMessages {
    SendHelloTo(ActorId),
    SendHelloReply,
}
