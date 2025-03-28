import 'package:filmes/models/filme.dart';
import 'package:filmes/models/genero.dart';
import 'package:flutter/foundation.dart';

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
      for (var filme in genero.filmes) {
        if (filme.id == filmeId) {
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
}
