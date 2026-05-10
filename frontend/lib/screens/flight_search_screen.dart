import 'package:flutter/material.dart';
import '../widgets/flight_card.dart';
import '../services/api_service.dart';

class FlightSearchScreen extends StatefulWidget {
  const FlightSearchScreen({Key? key}) : super(key: key);

  @override
  State<FlightSearchScreen> createState() => _FlightSearchScreenState();
}

class _FlightSearchScreenState extends State<FlightSearchScreen> {
  final _originController = TextEditingController();
  final _destinationController = TextEditingController();
  final _dateController = TextEditingController();
  List<dynamic> _flights = [];
  bool _loading = false;

  Future<void> _search() async {
    setState(() => _loading = true);
    final flights = await ApiService.searchFlights(
      origin: _originController.text,
      destination: _destinationController.text,
      date: _dateController.text,
    );
    setState(() {
      _flights = flights;
      _loading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Search Flights')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _originController,
              decoration: const InputDecoration(labelText: 'Origin'),
            ),
            TextField(
              controller: _destinationController,
              decoration: const InputDecoration(labelText: 'Destination'),
            ),
            TextField(
              controller: _dateController,
              decoration: const InputDecoration(labelText: 'Date (YYYY-MM-DD)'),
            ),
            const SizedBox(height: 16),
            ElevatedButton(onPressed: _search, child: const Text('Search')),
            const SizedBox(height: 16),
            _loading
                ? const CircularProgressIndicator()
                : Expanded(
                    child: ListView.builder(
                      itemCount: _flights.length,
                      itemBuilder: (context, index) {
                        return FlightCard(flight: _flights[index]);
                      },
                    ),
                  ),
          ],
        ),
      ),
    );
  }
}
