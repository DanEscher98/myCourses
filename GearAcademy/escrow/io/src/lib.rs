#![no_std]
use gmeta::{In, InOut, Metadata, Out};
use gstd::{msg, prelude::*, ActorId};

#[derive(Default, Encode, Decode, TypeInfo)]
pub struct Escrow {
    pub seller: ActorId,
    pub buyer: ActorId,
    pub price: u128,
    pub state: EscrowState,
}

impl Escrow {
    /// It validates:
    /// - Escrow state is AwaitingPayment
    /// - Sender's address match buyer's address
    /// - Attached funds equal the product price
    ///
    /// Then:
    /// - Updates Escrow state to AwaitingDelivery
    /// - Sends message FundsDeposited
    pub fn deposit(&mut self) {
        assert_eq!(
            self.state,
            EscrowState::AwaitingPayment,
            "State must be `AwaitingPayment`"
        );
        assert_eq!(
            msg::source(),
            self.buyer,
            "The message sender must be a buyer"
        );
        assert_eq!(
            msg::value(),
            self.price,
            "The attached value must be equal to set price"
        );
        self.state = EscrowState::AwaitingDelivery;
        msg::reply(EscrowEvent::FundsDeposited, 0)
            .expect("Error in reply EscrowEvent::FundsDeposited");
    }
    /// It validates:
    /// - EscrowState is AwaitingDelivery
    /// - Sender's address match buyer's address
    ///
    /// Then:
    /// - Upadtes Escrow state to Closed
    /// - Sends funds to the seller
    /// - Sends message DeliveryConfirmed
    pub fn confirm_delivery(&mut self) {
        assert_eq!(
            self.state,
            EscrowState::AwaitingDelivery,
            "State must be `AwaitingDelivery`"
        );
        assert_eq!(
            msg::source(),
            self.buyer,
            "The message sender must be a buyer"
        );
        self.state = EscrowState::Closed;
        msg::send(self.seller, EscrowEvent::FundsDeposited, self.price)
            .expect("Error sending the funds to `seller`");
        msg::reply(EscrowEvent::DeliveryConfirmed, 0)
            .expect("Error in reply EscrowEvent::DeliveryConfirmed");
    }
}

#[derive(Decode, Encode, TypeInfo)]
pub struct InitEscrow {
    pub seller: ActorId,
    pub buyer: ActorId,
    pub price: u128,
}

#[derive(Default, Debug, PartialEq, Eq, Encode, Decode, TypeInfo)]
pub enum EscrowState {
    #[default]
    AwaitingPayment,
    AwaitingDelivery,
    Closed,
}

#[derive(Decode, Encode, TypeInfo)]
pub enum EscrowAction {
    Deposit,
    ConfirmDelivery,
}

#[derive(Decode, Encode, TypeInfo)]
pub enum EscrowEvent {
    FundsDeposited,
    DeliveryConfirmed,
}

pub struct ProgramMetadata;
impl Metadata for ProgramMetadata {
    type Init = In<InitEscrow>;
    type Handle = InOut<EscrowAction, EscrowEvent>;
    type State = Out<Escrow>;
    type Reply = ();
    type Others = ();
    type Signal = ();
}
