import 'package:filmes/models/filme.dart';
import 'package:filmes/models/genero.dart';
import 'package:flutter/foundation.dart';
import 'package:logger/logger.dart';

class GenerosSingleton {
  // Private static instance
  static final GenerosSingleton _instance = GenerosSingleton._internal();

  // ValueNotifier to provide reactive updates
  final ValueNotifier<List<Genero>> generosNotifier =
      ValueNotifier<List<Genero>>([]);

  // Private constructor
  GenerosSingleton._internal();

  // Public factory constructor
  factory GenerosSingleton() {
    return _instance;
  }

  // Getter for the list of generos
  List<Genero> get generos => generosNotifier.value;

  // Method to add a genre
  void addGenero(Genero genero) {
    final currentGeneros = List<Genero>.from(generosNotifier.value);
    currentGeneros.add(genero);
    generosNotifier.value = currentGeneros;
  }

  // Method to remove a genre
  void removeGenero(Genero genero) {
    final currentGeneros = List<Genero>.from(generosNotifier.value);
    currentGeneros.remove(genero);
    generosNotifier.value = currentGeneros;
  }

  Genero? findGeneroById(String id) {
    if (generos.any((genero) => genero.id == id)) {
      return generos.firstWhere((genero) => genero.id == id);
    }
    return null;
  }

  Genero? findGeneroByNome(String nome) {
    if (generos.any((genero) => genero.nome == nome)) {
      return generos.firstWhere((genero) => genero.nome == nome);
    }
    return null;
  }

  void updateGenero(Genero genero) {
    final currentGeneros = List<Genero>.from(generosNotifier.value);
    final index = currentGeneros.indexWhere((g) => g.id == genero.id);
    currentGeneros[index] = genero;
    generosNotifier.value = currentGeneros;
  }

  Filme? findFilmeByFilmeId(String filmeId) {
    for (var genero in generos) {
      Logger().d("Logger is working! ${genero.nome}");
      for (var filme in genero.filmes) {
        if (filme.id == filmeId) {
          Logger().d("Encontrou ${filme.titulo}");
          return filme;
        }
      }
    }
    return null;
  }

  void updateFilme(Filme filme) {
    final currentGeneros = List<Genero>.from(generosNotifier.value);
    for (var genero in currentGeneros) {
      final index = genero.filmes.indexWhere((f) => f.id == filme.id);
      if (index != -1) {
        genero.filmes[index] = filme;
        generosNotifier.value = currentGeneros;
        return;
      }
    }
  }

  void updateFilmeOnGenero(Filme filme) {
    Logger().d("Adicionando filme ${filme.titulo} ao gênero ${filme.genero}");
    final currentGeneros = List<Genero>.from(generosNotifier.value);
    for (var genero in currentGeneros) {
      final index = genero.filmes.indexWhere((f) => f.id == filme.id);
      if (index != -1) {
        genero.filmes.removeAt(index);
        Logger().d("Removei o filme ${filme.titulo} do gênero ${genero.nome}");
      }
    }
    for (var genero in currentGeneros) {
      if (genero.nome == filme.genero) {
        genero.filmes.add(filme);
        generosNotifier.value = currentGeneros;
        return;
      }
    }

    // If the genre is not found, append a new genre with that name and add the movie
    Genero newGenero = Genero(
      id: filme.genero,
      nome: filme.genero,
      filmes: [filme],
    );
    currentGeneros.add(newGenero);
    generosNotifier.value = currentGeneros;
    Logger().d("Adicionou o filme ${filme.titulo} ao gênero ${filme.genero}");
  }
}
