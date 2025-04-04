import 'package:filmes/models/filme.dart';
import 'package:filmes/models/genero.dart';
import 'package:filmes/states/generos_state.dart';
import 'package:flutter/material.dart';

class FilmesPage extends StatelessWidget {
  const FilmesPage({super.key});

  @override
  Widget build(BuildContext context) {
    String gerenoId = ModalRoute.of(context)!.settings.arguments as String;
    Genero staticGenero = GenerosSingleton().findGeneroById(gerenoId)!;

    return Scaffold(
      appBar: AppBar(title: Text('filmes do gênero ${staticGenero.nome} ')),
      body: ValueListenableBuilder<List<Genero>>(
        valueListenable: GenerosSingleton().generosNotifier,
        builder: (context, generos, child) {
          Genero genero = generos.firstWhere((genero) => genero.id == gerenoId);
          return ListView.builder(
            itemCount: genero.filmes.length,
            itemBuilder: (context, index) {
              Filme filme = genero.filmes[index];
              return ListTile(
                title: Text(filme.titulo),
                subtitle: Text(filme.diretor),
                trailing: Text(filme.genero),
                onTap: () {
                  Navigator.of(context).pushNamed(
                    '/filmes/detalhe',
                    arguments: {'filmeId': filme.id},
                  );
                },
              );
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.of(
            context,
          ).pushNamed('/filmes/novo', arguments: {'generoId': staticGenero.id});
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}
