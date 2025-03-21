import funcionarios.models.Cargo;
import funcionarios.models.Funcionario;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");

        new Funcionario(
            1,
            "João",
            1000.0,
            Cargo.DESENVOLVEDOR_JUNIOR
        );
    }
}
