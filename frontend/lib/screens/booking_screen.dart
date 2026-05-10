import 'package:flutter/material.dart';
import 'package:international_flight_booking/services/api_service.dart';

class BookingScreen extends StatefulWidget {
  final Flight flight;
  const BookingScreen({super.key, required this.flight});

  @override
  State<BookingScreen> createState() => _BookingScreenState();
}

class _BookingScreenState extends State<BookingScreen> {
  final _nameController = TextEditingController();
  final _passportController = TextEditingController();
  bool _isLoading = false;

  Future<void> _book() async {
    setState(() {
      _isLoading = true;
    });
    try {
      final booking = await ApiService.bookFlight(
        flightId: widget.flight.id,
        passengerName: _nameController.text,
        passportNumber: _passportController.text,
      );
      Navigator.pushReplacementNamed(
        context,
        '/confirmation',
        arguments: booking,
      );
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Booking failed: $e')),
      );
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  void dispose() {
    _nameController.dispose();
    _passportController.dispose();
    super.dispose();
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
            Text('Flight: ${widget.flight.flightNumber}'),
            const SizedBox(height: 16),
            TextField(
              controller: _nameController,
              decoration: const InputDecoration(labelText: 'Passenger Name'),
            ),
            TextField(
              controller: _passportController,
              decoration: const InputDecoration(labelText: 'Passport Number'),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: _book,
              child: _isLoading
                  ? const SizedBox(
                      width: 20,
                      height: 20,
                      child: CircularProgressIndicator(
                        strokeWidth: 2,
                        color: Colors.white,
                      ),
                    )
                  : const Text('Confirm Booking'),
            ),
          ],
        ),
      ),
    );
  }
}
