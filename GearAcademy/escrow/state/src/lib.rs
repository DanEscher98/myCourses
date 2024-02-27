#![no_std]
use escrow_io::{EscrowState, ProgramMetadata};
use gmeta::{metawasm, Metadata};
use gstd::{prelude::*, ActorId};

#[cfg(feature = "binary-vendor")]
include!(concat!(env!("OUT_DIR"), "/wasm_binary.rs"));

#[metawasm]
pub mod metafns {
    pub type State = <ProgramMetadata as Metadata>::State;

    pub fn seller(state: State) -> ActorId {
        state.1.seller
    }
    pub fn buyer(state: State) -> ActorId {
        state.1.buyer
    }
    pub fn escrow_state(state: State) -> EscrowState {
        state.1.state
    }
}
