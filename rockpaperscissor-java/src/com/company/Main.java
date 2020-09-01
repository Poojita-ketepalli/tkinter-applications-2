package com.company;

import java.util.*;

public class Main {

    public static void main(String[] args) {
		String choice_name;
		String comp_choice_name;
		String result;
		int yourscore=0;
		int comp_score=0;
	    System.out.println("Winning Rules of game are as follows:\n  1.Rock Vs paper->Paper wins \n  2.Rock Vs Scissor->Rock wins \n  3.Paper Vs Scissor->Scissor wins \n");
	    while(true){
	        System.out.println("Enter your choice:\n " + "1.Rock\n  2.Paper\n  3.Scissor");
	        Scanner s = new Scanner(System.in);
			int choice=s.nextInt();
			while(choice>3 || choice<1){
				System.out.println("Enter valid number");
				choice=s.nextInt();
			}
			if(choice==1){
				choice_name = "Rock";
			}
			else if(choice==2){
				choice_name = "Paper";
			}
			else{
				choice_name = "Scissor";
			}
			System.out.println("Your choice is :"+ choice_name);
			// computer game
			Random rand = new Random();
			int comp_choice=rand.nextInt(3);
			if(comp_choice==1){
				comp_choice_name = "Rock";
			}
			else if(comp_choice==2){
				comp_choice_name = "Paper";
			}
			else{
				comp_choice_name = "Scissor";
			}
			System.out.println("Computer's choice is :"+ comp_choice_name);

			if((choice==1 && comp_choice==2) || (choice==2 && comp_choice==1)) {
				result = "Paper";
			}
			else if((choice==1 && comp_choice==3) || (choice==3 && comp_choice==1)){
				result = "Rock";
			}
    		else{
				result = "Scissor";
			}
			if(result.equals(choice_name)) {
				System.out.println("<==USER WINS==>");
				yourscore+=1;
			}
			else if(choice_name.equals(comp_choice_name)) {
				System.out.println("<==THE MATCH IS TIE==>");
			}
    		else {
				System.out.println("<==COMPUTER WINS==>");
				comp_score+=1;
			}
			System.out.println("YOUR SCORE:"+yourscore);
			System.out.println("COMPUTER'S SCORE"+comp_score);
			System.out.println("DO YOU WANT TO PLAY AGAIN?(Y/N)");
			String ans=s.next();
			if(ans.equals("n") || ans.equals("N")){
				System.out.println("THANKS FOR PLAYING:)");
				break;
			}
		}
    }
}
