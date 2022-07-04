package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Deck[C Card] struct {
	cards []C
}

type Card interface {
	fmt.Stringer
	Name() string
}

func printCard[C Card](card C) {
	fmt.Println("card name: ", card.Name())
}

func (deck *Deck[C]) AddCard(card C) {
	deck.cards = append(deck.cards, card)
}

func (deck *Deck[C]) RandomCard() C {
	card := rand.New(rand.NewSource(time.Now().UnixNano()))
	cardIndex := card.Intn(len(deck.cards))
	return deck.cards[cardIndex]
}

type PlayingCard struct {
	Suit string
	Rank string
}

func (pc *PlayingCard) String() string {
	return fmt.Sprintf("%s of %s", pc.Rank, pc.Suit)
}

func (pc *PlayingCard) Name() string {
	return pc.String()
}

func NewPlayingCard(suit string, card string) *PlayingCard {
	return &PlayingCard{Suit: suit, Rank: card}
}

func NewPlayingCardDeck() *Deck[*PlayingCard] {
	suits := []string{"Diamonds", "Hearts", "Clubs", "Spades"}
	ranks := []string{"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
	deck := &Deck[*PlayingCard]{}
	for _, suit := range suits {
		for _, rank := range ranks {
			deck.AddCard(NewPlayingCard(suit, rank))
		}
	}
	return deck
}

type TradingCard struct {
	CollectableName string
}

func (tc *TradingCard) String() string {
	return tc.CollectableName
}

func (tc *TradingCard) Name() string {
	return tc.String()
}

func NewTradingCard(collectableName string) *TradingCard {
	return &TradingCard{CollectableName: collectableName}
}

func NewTradingCardDeck() *Deck[*TradingCard] {
	collectables := []string{"Sammy", "Droplets", "Spaces", "App Platform"}
	deck := &Deck[*TradingCard]{}
	for _, collectable := range collectables {
		deck.AddCard(NewTradingCard(collectable))
	}
	return deck
}

func main() {
	playingDeck := NewPlayingCardDeck()
	fmt.Printf("--- drawing playing card ---\n")
	playingCard := playingDeck.RandomCard()
	fmt.Printf("drew card: %s\n", playingCard)

	tradingDeck := NewTradingCardDeck()
	fmt.Printf("--- drawing trading card ---\n")
	tradingCard := tradingDeck.RandomCard()
	fmt.Printf("drew card: %s\n", tradingCard)

	fmt.Printf("--- printing cards ---\n")
	printCard(playingCard)
	printCard(tradingCard)
}

/* REREFERENCES
- https://www.digitalocean.com/community/tutorial_series/how-to-code-in-go
- https://www.digitalocean.com/community/tutorials/how-to-use-generics-in-go
*/
