import 'package:filmes/models/filme.dart';
import 'package:filmes/states/generos_state.dart';
import 'package:flutter/material.dart';
import 'package:uuid/uuid.dart';

class FilmePage extends StatefulWidget {
  const FilmePage({super.key});

  @override
  State<FilmePage> createState() => _FilmePageState();
}

class _FilmePageState extends State<FilmePage> {
  final TextEditingController _idController = TextEditingController(
    text: Uuid().v4(),
  );
  final TextEditingController _tituloController = TextEditingController();
  final TextEditingController _diretorController = TextEditingController();
  final TextEditingController _generoController = TextEditingController();

  final _formKey = GlobalKey<FormState>();
  @override
  Widget build(BuildContext context) {
    Map filmeId = ModalRoute.of(context)!.settings.arguments as Map;

    Filme? filme = GenerosSingleton().findFilmeByFilmeId(filmeId['filmeId']);

    return Scaffold(
      appBar: AppBar(title: Text('Detalhes do filme $filmeId')),
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
              TextFormField(
                decoration: const InputDecoration(labelText: 'Gênero'),
                controller: _generoController,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Nome é obrigatório';
                  }
                  return null;
                },
              ),
              ElevatedButton(
                onPressed:
                    () => {
                      if (_formKey.currentState!.validate())
                        {
                          ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(content: Text('Criando...')),
                          ),
                          if (filme != null)
                            {
                              GenerosSingleton().updateFilme(
                                filme.copyWith(
                                  id: _idController.text,
                                  titulo: _tituloController.text,
                                  diretor: _diretorController.text,
                                  genero: _generoController.text,
                                ),
                              ),
                              Navigator.of(context).pop(),
                            },
                          if (filme == null)
                            {
                              GenerosSingleton().updateFilme(
                                Filme(
                                  id: _idController.text,
                                  titulo: _tituloController.text,
                                  diretor: _diretorController.text,
                                  genero: _generoController.text,
                                ),
                              ),
                              Navigator.of(context).pop(),
                            },
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
