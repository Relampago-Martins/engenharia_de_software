package funcionarios.dao;

import java.lang.System.Logger;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

import funcionarios.models.Funcionario;


public class FuncionarioDAO {
	
	private static final Logger logger = System.getLogger(FuncionarioDAO.class.getName());

	public void salva(Funcionario funcionario) throws SQLException{

		ConnectionDAO connectionDAO = new ConnectionDAO("root", "");
		connectionDAO.setDbms("mysql");
		connectionDAO.setServerName("localhost");
		connectionDAO.setPortNumber("8080");
		connectionDAO.setDbName("mock");
	   
		try (Connection connection = connectionDAO.createConnection();
			 Statement stmt = connection.createStatement();) {
			
			String sql = "insert into funcionario (id, nome, salario) values (" + funcionario.getId() + "," +
					funcionario.getNome() + "," + funcionario.getSalario() + ")";
			int rs = stmt.executeUpdate(sql);
			
			if (rs == 1){
				logger.log(System.Logger.Level.INFO, "Funcionario inserido com sucesso.");
			}
		} catch (SQLException e) {
			logger.log(System.Logger.Level.ERROR, "Erro ao inserir funcionario: " + e.getMessage());
		}
	}
}