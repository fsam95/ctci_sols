public class Card {

  public enum Suit {
      HEARTS, SPADES, CLUBS, DIAMONDS 

      public String toString(){
          case HEARTS:
            return "<3"; 
            break;
          case DIAMONDS: 
            return "<>"; 
            break;
          case CLUBS:
            return "clubs";
            break;
          case SPADES:
            return "spades";
            break;
      }
  }
  
  private int value;
  private Suit suit;
  public Card(value, suit){
    this.value = value;
    this.suit = suit;
  }

  public String toString(){
    return String.valueOf(this.value) + this.suit;
  }

  public static void main(String[] args){
    System.out.println(Card(5, Card.Suit.HEARTS));
  }
}

