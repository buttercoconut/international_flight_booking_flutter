import 'package:flutter/material.dart';

class ErrorScreen extends StatelessWidget {
  static const routeName = '/error';

  const ErrorScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Error')),
      body: const Center(
        child: Text(
          'An unexpected error occurred. Please try again later.',
          textAlign: TextAlign.center,
          style: TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}
