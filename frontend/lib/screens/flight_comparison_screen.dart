import 'package:flutter/material.dart';
import 'package:international_flight_booking/services/api_service.dart';
import 'package:international_flight_booking/widgets/flight_card.dart';

class FlightComparisonScreen extends StatefulWidget {
  final Flight flight;
  const FlightComparisonScreen({super.key, required this.flight});

  @override
  State<FlightComparisonScreen> createState() => _FlightComparisonScreenState();
}

class _FlightComparisonScreenState extends State<FlightComparisonScreen> {
  List<Flight> _alternatives = [];
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _fetchAlternatives();
  }

  Future<void> _fetchAlternatives() async {
    setState(() {
      _isLoading = true;
    });
    try {
      final alternatives = await ApiService.getAlternativeFlights(
        origin: widget.flight.origin,
        destination: widget.flight.destination,
        date: widget.flight.date,
      );
      setState(() {
        _alternatives = alternatives;
      });
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error fetching alternatives: $e')),
      );
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Compare Flights'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Selected Flight',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            FlightCard(flight: widget.flight),
            const SizedBox(height: 16),
            const Text(
              'Alternative Flights',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            if (_isLoading)
              const Center(child: CircularProgressIndicator()),
            Expanded(
              child: ListView.builder(
                itemCount: _alternatives.length,
                itemBuilder: (context, index) {
                  final alt = _alternatives[index];
                  return FlightCard(
                    flight: alt,
                    onTap: () {
                      Navigator.pushReplacementNamed(
                        context,
                        '/booking',
                        arguments: alt,
                      );
                    },
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
