import 'package:flutter/material.dart';
import 'package:international_flight_booking/services/api_service.dart';
import 'package:provider/provider.dart';

class BookingScreen extends StatefulWidget {
  const BookingScreen({Key? key}) : super(key: key);

  @override
  State<BookingScreen> createState() => _BookingScreenState();
}

class _BookingScreenState extends State<BookingScreen> {
  final _nameController = TextEditingController();
  final _passportController = TextEditingController();
  final _emailController = TextEditingController();
  bool _isSubmitting = false;

  @override
  void dispose() {
    _nameController.dispose();
    _passportController.dispose();
    _emailController.dispose();
    super.dispose();
  }

  Future<void> _submitBooking() async {
    setState(() {
      _isSubmitting = true;
    });
    final api = Provider.of<ApiService>(context, listen: false);
    final success = await api.bookFlight(
      passengerName: _nameController.text,
      passportNumber: _passportController.text,
      email: _emailController.text,
    );
    setState(() {
      _isSubmitting = false;
    });
    if (success) {
      Navigator.pushReplacementNamed(context, '/confirmation');
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Booking failed. Please try again.')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Book Flight'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _nameController,
              decoration: const InputDecoration(labelText: 'Full Name'),
            ),
            TextField(
              controller: _passportController,
              decoration: const InputDecoration(labelText: 'Passport Number'),
            ),
            TextField(
              controller: _emailController,
              decoration: const InputDecoration(labelText: 'Email'),
            ),
            const SizedBox(height: 20),
            _isSubmitting
                ? const CircularProgressIndicator()
                : ElevatedButton(
                    onPressed: _submitBooking,
                    child: const Text('Confirm Booking'),
                  ),
          ],
        ),
      ),
    );
  }
}
