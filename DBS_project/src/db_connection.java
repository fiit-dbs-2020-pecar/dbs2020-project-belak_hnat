
import javax.swing.*;
import java.sql.*;

public class db_connection {
    public Connection c = null;

    public db_connection(){
        try {
            Class.forName("org.postgresql.Driver");
            c = DriverManager.getConnection("jdbc:postgresql://localhost:5432/myDB","postgres" , "projectheslo98" );//postgres,Mkoijn12
            c.setAutoCommit(true);
            JOptionPane.showMessageDialog(null, "Uspesne spojenie s databazou", "", JOptionPane.INFORMATION_MESSAGE);

        } catch ( Exception e ) {
            JOptionPane.showMessageDialog(null, "Neuspesne spojenie s databazou", "", JOptionPane.ERROR_MESSAGE);
        }
    }
}

