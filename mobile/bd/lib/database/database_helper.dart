import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

import '/database/sqls/pessoa_sql.dart';

class DatabaseHelper {
  static final String _nomeBancoDeDados = "meubanco.db";
  static final int _versaoBancoDeDados = 2;
  static Database? _bancoDeDados;

  // Getter para acesso lazy ao banco de dados
  Future<Database> get bancoDeDados async {
    if (_bancoDeDados != null) {
      return _bancoDeDados!;
    }
    // Se o banco de dados ainda não foi inicializado, inicializa-o
    _bancoDeDados = await init();
    return _bancoDeDados!;
  }

  init() async {
    String caminhoBanco = join(await getDatabasesPath(), _nomeBancoDeDados);
    _bancoDeDados = await openDatabase(
      caminhoBanco,
      version: _versaoBancoDeDados,
      onCreate: criarBD,
      onUpgrade: atualizaBD,
    );
  }

  Future criarBD(Database db, int versao) async {
    db.execute(PessoaSql.criarTabelaPessoa());
  }

  Future atualizaBD(Database db, int oldVersion, int newVersion) async {
    if (newVersion == 2) {}
  }

  Future<int> inserir(String tabela, Map<String, Object?> valores) async {
    final db = await bancoDeDados;
    return await db.insert(tabela, valores);
  }

  Future<List<Map<String, Object?>>> getAll(
    String tabela, {
    String? condicao,
    List<Object>? conidcaoArgs,
  }) async {
    final db = await bancoDeDados;
    return await db.query(tabela, where: condicao, whereArgs: conidcaoArgs);
  }

  Future<Map<String, Object?>> getOne(
    String tabela, {
    String? condicao,
    List<Object>? conidcaoArgs,
  }) async {
    final db = await bancoDeDados;
    var resultado = await db.query(
      tabela,
      where: condicao,
      whereArgs: conidcaoArgs,
    );
    return resultado.first;
  }
}
