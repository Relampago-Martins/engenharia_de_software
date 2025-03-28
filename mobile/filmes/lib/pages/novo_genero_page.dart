import 'package:filmes/models/genero.dart';
import 'package:filmes/states/generos_state.dart';
import 'package:flutter/material.dart';
import 'package:uuid/uuid.dart';

class NovoGeneroPage extends StatefulWidget {
  const NovoGeneroPage({super.key});

  @override
  State<NovoGeneroPage> createState() => _NovoGeneroPageState();
}

class _NovoGeneroPageState extends State<NovoGeneroPage> {
  final TextEditingController _idController = TextEditingController(
    text: Uuid().v4(),
  );
  final TextEditingController _nomeController = TextEditingController();

  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Novo Gênero')),
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
                decoration: const InputDecoration(labelText: 'Nome'),
                controller: _nomeController,
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
                            const SnackBar(content: Text('Salvando...')),
                          ),
                          GenerosSingleton().addGenero(
                            Genero(
                              id: _idController.text,
                              nome: _nomeController.text,
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
