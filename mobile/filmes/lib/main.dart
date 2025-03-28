import 'package:filmes/pages/filme_page.dart';
import 'package:filmes/pages/filmes_page.dart';
import 'package:filmes/pages/generos_page.dart';
import 'package:filmes/pages/novo_filme_page.dart';
import 'package:filmes/pages/novo_genero_page.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Filmes',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => const GenerosPage(),
        '/generos/novo': (context) => const NovoGeneroPage(),
        '/filmes': (context) => const FilmesPage(),
        '/filmes/detalhe': (context) => const FilmePage(),
        '/filmes/novo': (context) => const NovoFilmePage(),
      },
    );
  }
}
