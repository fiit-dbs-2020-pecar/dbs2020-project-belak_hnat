import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JTable;
import javax.swing.table.*;
import java.sql.*;

public class GUI_zakaznik {
    private JPanel main_Panel;
    private JTable tbl_data;
    private JButton add_item_btn;



    public Connection db_c;
    public Statement db_s;

    private GUI_zakaznik ja;

    public JPanel getMain_Panel(){
        return main_Panel;
    }

    public GUI_zakaznik(db_connection db_c) {
        this.db_c = db_c.c;

        ja = this;
        updateTableModel();

        add_item_btn.addActionListener(new ActionListener() { // pridavanie zaznamu
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                JFrame frame = new JFrame("Insert a new item");
                gui_insert_customers menu = new gui_insert_customers();
                menu.setBaseframe(frame);
                menu.setGuimenu(ja);
                frame.setContentPane(menu.getMain_panel());
                frame.pack();
                frame.setSize(400, 300);
                frame.setLocationRelativeTo(null);
                frame.setVisible(true);
            }
        });

    }


    public void updateTableModel() {

        DefaultTableModel defmodel = new DefaultTableModel() {
            @Override
            public boolean isCellEditable(int row, int column) {
                //all cells false
                return false;
            }
        };


        defmodel.addColumn("Surname");
        defmodel.addColumn("Name");
        defmodel.addColumn("Titul");
        defmodel.addColumn("tesl.cislo");
        defmodel.addColumn("E-Mail Address");

        tbl_data.setModel(defmodel);
        tbl_data.getTableHeader().setReorderingAllowed(false);
        tbl_data.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);

        updateTableData();
    }

    private void updateTableData() {

        String queryText = "SELECT * FROM (SELECT * FROM " + "zakaznik" + " ORDER BY id ASC) AS t ";
        String queryText_Having = "";

        try {
            db_s = db_c.createStatement();
            ResultSet rs = db_s.executeQuery(queryText);
            DefaultTableModel mdl = (DefaultTableModel) tbl_data.getModel();
            while (rs.next()) {
                mdl.addRow(new Object[]{
                        rs.getInt("id"),
                        rs.getString("meno"),
                        rs.getString("priezvisko"),
                        rs.getString("titul"),
                        rs.getString("tel_cislo"),
                        rs.getString("email"),
                });
            }

            rs.close();
            db_s.close();
        } catch (Exception e) {
            showErrorDialogPopup(e);
        }
    }

    public void showErrorDialogPopup(Exception e) {
        JOptionPane.showMessageDialog(main_Panel, e, "Error", JOptionPane.ERROR_MESSAGE);
    }

    public void try_send(String queryText, JFrame baseframe) {
        try {
            db_s = db_c.createStatement();
            db_s.executeUpdate(queryText);

            db_s.close();
            updateTableModel();
            baseframe.dispose();
        } catch (Exception e) {
            showErrorDialogPopup(e);
        }
    }




}
