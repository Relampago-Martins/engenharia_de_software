import 'package:filmes/models/filme.dart';
import 'package:filmes/models/genero.dart';
import 'package:filmes/states/generos_state.dart';
import 'package:flutter/material.dart';
import 'package:uuid/uuid.dart';

class NovoFilmePage extends StatefulWidget {
  const NovoFilmePage({super.key});

  @override
  State<NovoFilmePage> createState() => _NovoFilmePageState();
}

class _NovoFilmePageState extends State<NovoFilmePage> {
  final TextEditingController _idController = TextEditingController(
    text: Uuid().v4(),
  );
  final TextEditingController _tituloController = TextEditingController();
  final TextEditingController _diretorController = TextEditingController();

  final _formKey = GlobalKey<FormState>();
  @override
  Widget build(BuildContext context) {
    Map args = ModalRoute.of(context)!.settings.arguments as Map;
    Genero genero = GenerosSingleton().findGeneroById(args['generoId'])!;

    return Scaffold(
      appBar: AppBar(title: const Text('Novo Filme')),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
        child: Form(
          key: _formKey,
          child: ListView(
            children: [
              TextFormField(
                decoration: const InputDecoration(labelText: 'ID'),
                keyboardType: TextInputType.number,
                controller: _idController,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'ID é obrigatório';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),

              TextFormField(
                decoration: const InputDecoration(labelText: 'Título'),
                controller: _tituloController,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Nome é obrigatório';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                decoration: const InputDecoration(labelText: 'Diretor'),
                controller: _diretorController,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Nome é obrigatório';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),

              ElevatedButton(
                onPressed:
                    () => {
                      if (_formKey.currentState!.validate())
                        {
                          ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(content: Text('Criando...')),
                          ),
                          GenerosSingleton().updateGenero(
                            genero.copyWith(
                              filmes: [
                                ...genero.filmes,
                                Filme(
                                  id: _idController.text,
                                  titulo: _tituloController.text,
                                  diretor: _diretorController.text,
                                  genero: genero.nome,
                                ),
                              ],
                            ),
                          ),
                          Navigator.of(context).pop(),
                        },
                    },
                child: Text('Salvar'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
