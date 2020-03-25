import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import java.sql.*;

public class Main_db {




    public Main_db() {
        db_connection db_c;
        db_c = new db_connection();

        if(db_c.c != null){
            JFrame frame = new JFrame("Database menu");
            GUI_zakaznik menu = new GUI_zakaznik(db_c);
            frame.setContentPane(menu.getMain_Panel());
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.pack();
            frame.setSize(800, 600);
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        }
    }

    public static void main(String[] args) {
       new Main_db();
    }

}
