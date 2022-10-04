package oo.workflow;

import oo.data.ConsoleStatus;
import java.util.ArrayList;

public class Console {
    boolean exit;
    int returnCode;
    ConsoleStatus status;
    public int init(){
        exit=false;
        return 0;
    }
    public ConsoleStatus getStaus(){
        return null;
    }
    public ArrayList<String> getCommand(){
        return null;
    }
    public Command parseCommand(ArrayList<String> cmd){
        return null;
    }
    public int mainProcess(){
        while(exit){
            ArrayList<String> command = getCommand();
            parseCommand(command).excute();
        }
        return returnCode;
    }
    private int exit(){
        exit=true;
        return 0;
    }
}
