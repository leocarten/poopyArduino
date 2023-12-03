bool first_move = false;
int x_move_from = 1;
int x_move_to = 0;

int y_move_from = 1;
int y_move_to = 0;

// 145 is 1 inch !!

// Things to solve 
//  - What to do if we eliminate a piece?
//  - How will we take control of the arm?

void setup() {
  // Start at h1
  Serial.begin(9600);
}

int x_direction(String move, bool if_first_move, bool if_piece_captured){
  int val_to_return = 0;
  if(if_first_move){ 
    // move from h1 to new value
    char x_movement = move[1];
    int intDigit = x_movement - '0'; // convert char to int
    // move from 
    // Serial.println(x_move_from);
    // Serial.println(intDigit);
    if(x_move_from == intDigit){
      val_to_return = 0;
    }
    //      1 - 7
    else if(x_move_from - intDigit <= 0){
      val_to_return = (intDigit - x_move_from) * 145;
    }
    else{
      // 6 - 5
      val_to_return = (intDigit - x_move_from) * 145;
    }
    if(val_to_return != 0){
      x_move_from = intDigit;
    }
  }
  // need a case for when we need to remove a piece
  else{
    char x_movement = move[1];
    int intDigit = x_movement - '0'; // convert char to int
    Serial.print("intDigit: ");
    Serial.println(intDigit);
    // Let's imagine the x_move_from is 8
    // Let's imagine the intDigit is 4

    if(x_move_from == intDigit){
      val_to_return = 0;
    }
    //.    7 4
    else if(x_move_from < intDigit){
        // Serial.println("Moving up");
        val_to_return = (intDigit - x_move_from) * 145;
    }
    else{
        // Serial.println("Moving down");
        val_to_return = (x_move_from - intDigit) * -145;
    }


    if(val_to_return != 0){
      x_move_from = intDigit;
    }
  }

  return val_to_return;
}

int convertLetterToInt(char letter) {
  int result = 0;

  switch (letter) {
    case 'a': result = 8; break;
    case 'b': result = 7; break;
    case 'c': result = 6; break;
    case 'd': result = 5; break;
    case 'e': result = 4; break;
    case 'f': result = 3; break;
    case 'g': result = 2; break;
    case 'h': result = 1; break;
    default:  result = 0; break;
  }

  return result;
}

int y_direction(String move, bool if_first_move, bool if_piece_captured) {
  int val_to_return = 0;

  char y_movement = move[0];
  int letter_to_int = convertLetterToInt(y_movement);
  Serial.print("Letter to int: ");
  Serial.println(letter_to_int);

  // if (if_first_move) {
    if (letter_to_int == y_move_from) {
      val_to_return = 0;
      //.      3                2
    } else if (letter_to_int > y_move_from) {
      val_to_return = (letter_to_int - y_move_from) * 145;
    } else {
      val_to_return = (letter_to_int - y_move_from) * 145;
    }

    if(val_to_return != 0){
      y_move_from = letter_to_int;
    }

    // y_move_from = letter_to_int;
  // }
  // else{
  //   if (letter_to_int == y_move_from) {
  //     val_to_return = 0;
  //   } else if (letter_to_int > y_move_from) {
  //     val_to_return = (letter_to_int - y_move_from) * 145;
  //   } else {
  //     val_to_return = (letter_to_int - y_move_from) * -145;
  //   }

  //   y_move_from = letter_to_int;
  // }
  return val_to_return;
}

void loop() {
  if(!first_move){
    // We need to move from h1
    // Imagine we get the input g1h3 -> move from h1 to g1, get the piece, move to h3, release the piece
    // The next input is a7a5 -> move from h3 to a7, drop down, get the piece, move to a5
    int x = x_direction("g1", true, true);
    int y = y_direction("g1", true, true);
    Serial.print("The x value returned was: ");
    Serial.println(x);
    Serial.print("The y value returned was: ");
    Serial.println(y);
    Serial.println("------------------------------");
    Serial.println("Grab the piece");
    int xx = x_direction("h3", false, true);
    int yy = y_direction("h3", false, true);
    Serial.print("The x value returned was: ");
    Serial.println(xx);
    Serial.print("The y value returned was: ");
    Serial.println(yy);
    Serial.println("------------------------------");

    Serial.println("Drop the piece");
    int xxx = x_direction("c7", false, true);
    int yyy = y_direction("c7", false, true);
    Serial.print("The x value returned was: ");
    Serial.println(xxx);
    Serial.print("The y value returned was: ");
    Serial.println(yyy);
    Serial.println("Drop the piece");
    Serial.println("------------------------------");

    int xxxx = x_direction("c4", false, true);
    int yyyy = y_direction("c4", false, true);
    Serial.print("The x value returned was: ");
    Serial.println(xxxx);
    Serial.print("The y value returned was: ");
    Serial.println(yyyy);
    Serial.println("Drop the piece");

    int xxxxx = x_direction("f3", false, true);
    int yyyyy = y_direction("f3", false, true);
    Serial.print("The x value returned was: ");
    Serial.println(xxxxx);
    Serial.print("The y value returned was: ");
    Serial.println(yyyyy);
    Serial.println("Drop the piece");

    int xxxxxx = x_direction("e5", false, true);
    int yyyyyy = y_direction("e5", false, true);
    Serial.print("The x value returned was: ");
    Serial.println(xxxxxx);
    Serial.print("The y value returned was: ");
    Serial.println(yyyyyy);
    Serial.println("Drop the piece");
  }
  first_move = true;
}

