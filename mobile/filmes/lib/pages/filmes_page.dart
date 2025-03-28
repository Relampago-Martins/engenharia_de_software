import 'package:filmes/models/filme.dart';
import 'package:filmes/models/genero.dart';
import 'package:filmes/states/generos_state.dart';
import 'package:flutter/material.dart';

class FilmesPage extends StatelessWidget {
  const FilmesPage({super.key});

  @override
  Widget build(BuildContext context) {
    String gerenoId = ModalRoute.of(context)!.settings.arguments as String;
    Genero genero = GenerosSingleton().findGeneroById(gerenoId)!;

    return Scaffold(
      appBar: AppBar(title: Text('filmes do gênero ${genero.nome} ')),
      body: ListView.builder(
        itemCount: genero.filmes.length,
        itemBuilder: (context, index) {
          Filme filme = genero.filmes[index];
          return ListTile(
            title: Text(filme.titulo),
            subtitle: Text(filme.diretor),
            trailing: Text(filme.genero),
            onTap: () {
              Navigator.of(
                context,
              ).pushNamed('/filmes/detalhe', arguments: {'filmeId': filme.id});
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.of(
            context,
          ).pushNamed('/filmes/novo', arguments: {'generoId': genero.id});
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}
