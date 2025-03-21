package funcionarios.models;

import funcionarios.utils.RegraDeCalculo;
import funcionarios.utils.RegraOnzePorcento;
import funcionarios.utils.RegraVinteDoisEMeioPorcento;

public enum Cargo {

	DESENVOLVEDOR_JUNIOR(new RegraOnzePorcento()),
	DESENVOLVEDOR_SENIOR(new RegraVinteDoisEMeioPorcento());
	
	private RegraDeCalculo regra;
	
	Cargo(RegraDeCalculo regra){
		this.regra = regra;
	}

	public RegraDeCalculo getRegra() {
		return regra;
	}
	
}