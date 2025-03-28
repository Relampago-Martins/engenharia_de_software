import 'package:filmes/models/filme.dart';

class Genero {
  String id;
  String nome;
  List<Filme> filmes;

  Genero({required this.id, required this.nome, this.filmes = const []});

  Genero copyWith({String? nome, List<Filme>? filmes}) {
    return Genero(
      id: id,
      nome: nome ?? this.nome,
      filmes: filmes ?? this.filmes,
    );
  }
}
