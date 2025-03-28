import 'package:filmes/models/genero.dart';
import 'package:filmes/states/generos_state.dart';
import 'package:flutter/material.dart';

class GenerosPage extends StatelessWidget {
  const GenerosPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Gêneros')),
      body: ValueListenableBuilder<List<Genero>>(
        valueListenable: GenerosSingleton().generosNotifier,
        builder: (context, generos, child) {
          return ListView.builder(
            itemCount: generos.length,
            itemBuilder: (context, index) {
              Genero genero = generos[index];
              return ListTile(
                title: Text(genero.nome),
                onTap: () {
                  Navigator.of(
                    context,
                  ).pushNamed('/filmes', arguments: genero.id);
                },
              );
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.of(context).pushNamed('/generos/novo');
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}
