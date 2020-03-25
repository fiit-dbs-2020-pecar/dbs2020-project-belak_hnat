import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.Statement;

public class gui_insert_customers {
    private JPanel main_panel;
    private JTextField field_customer_name;
    private JTextField field_customer_surname;
    private JButton confirmButton;
    private JTextField field_customer_email;
    private JTextField field_customer_titul;
    private JTextField field_customer_tel_cislo;

    private JFrame baseframe;
    private GUI_zakaznik guimenu;

    public Connection db_c;
    public Statement db_s;

    public JPanel getMain_panel(){
        return main_panel;
    }

    public void setBaseframe(JFrame baseframe){
        this.baseframe = baseframe;
    }

    public void setGuimenu( GUI_zakaznik guimenu ){
        this.guimenu = guimenu;
    }

    public gui_insert_customers() {
        //this.db_c=db_c;

        confirmButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                String queryText = "INSERT INTO zakaznik (meno, priezvisko, titul, tel_cislo, email) "
                        + "VALUES ('" + field_customer_name.getText() + "', '" + field_customer_surname.getText() + "', '" + field_customer_titul.getText() + "', '" + field_customer_tel_cislo.getText() +  "', '" + field_customer_email.getText() + "')";

                guimenu.try_send(queryText, baseframe);
            }
        });
    }

    private void try_send(String queryText){
        try {
            db_s = db_c.createStatement();
            db_s.executeUpdate(queryText);

            db_s.close();
            guimenu.updateTableModel();
            baseframe.dispose();
        } catch (Exception e) {
            guimenu.showErrorDialogPopup(e);
        }
    }

}
