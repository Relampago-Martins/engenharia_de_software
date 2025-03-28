class Filme {
  String id;
  String titulo;
  String diretor;
  String genero;

  Filme({
    required this.id,
    required this.titulo,
    required this.diretor,
    required this.genero,
  });

  Filme copyWith({
    String? id,
    String? titulo,
    String? diretor,
    String? genero,
  }) {
    return Filme(
      id: id ?? this.id,
      titulo: titulo ?? this.titulo,
      diretor: diretor ?? this.diretor,
      genero: genero ?? this.genero,
    );
  }
}
