import 'package:flutter/material.dart';

class BookingConfirmationScreen extends StatelessWidget {
  static const routeName = '/confirmation';

  const BookingConfirmationScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Booking Confirmation')),
      body: const Center(
        child: Text(
          'Your flight has been booked successfully!\nThank you for choosing us.',
          textAlign: TextAlign.center,
          style: TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}
