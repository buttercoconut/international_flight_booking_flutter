import 'package:flutter/material.dart';
import 'package:international_flight_booking/widgets/flight_card.dart';
import 'package:international_flight_booking/services/api_service.dart';
import 'package:provider/provider.dart';
import 'package:intl/intl.dart';

class FlightSearchScreen extends StatefulWidget {
  const FlightSearchScreen({Key? key}) : super(key: key);

  @override
  State<FlightSearchScreen> createState() => _FlightSearchScreenState();
}

class _FlightSearchScreenState extends State<FlightSearchScreen> {
  final _originController = TextEditingController();
  final _destinationController = TextEditingController();
  DateTime? _departureDate;
  int _passengers = 1;
  List<Flight> _searchResults = [];
  bool _isLoading = false;

  @override
  void dispose() {
    _originController.dispose();
    _destinationController.dispose();
    super.dispose();
  }

  Future<void> _searchFlights() async {
    setState(() {
      _isLoading = true;
    });
    final api = Provider.of<ApiService>(context, listen: false);
    final results = await api.searchFlights(
      origin: _originController.text,
      destination: _destinationController.text,
      departureDate: _departureDate,
      passengers: _passengers,
    );
    setState(() {
      _searchResults = results;
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Search Flights'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            TextField(
              controller: _originController,
              decoration: const InputDecoration(labelText: 'Origin'),
            ),
            TextField(
              controller: _destinationController,
              decoration: const InputDecoration(labelText: 'Destination'),
            ),
            Row(
              children: [
                Expanded(
                  child: Text(_departureDate == null
                      ? 'Select Departure Date'
                      : DateFormat.yMMMd().format(_departureDate!)),
                ),
                IconButton(
                  icon: const Icon(Icons.calendar_today),
                  onPressed: () async {
                    final date = await showDatePicker(
                      context: context,
                      initialDate: DateTime.now(),
                      firstDate: DateTime.now(),
                      lastDate: DateTime.now().add(const Duration(days: 365)),
                    );
                    if (date != null) {
                      setState(() {
                        _departureDate = date;
                      });
                    }
                  },
                ),
              ],
            ),
            Row(
              children: [
                const Text('Passengers:'),
                IconButton(
                  icon: const Icon(Icons.remove),
                  onPressed: () {
                    if (_passengers > 1) {
                      setState(() {
                        _passengers--;
                      });
                    }
                  },
                ),
                Text('$_passengers'),
                IconButton(
                  icon: const Icon(Icons.add),
                  onPressed: () {
                    setState(() {
                      _passengers++;
                    });
                  },
                ),
              ],
            ),
            ElevatedButton(
              onPressed: _searchFlights,
              child: const Text('Search'),
            ),
            const SizedBox(height: 16),
            _isLoading
                ? const Center(child: CircularProgressIndicator())
                : Expanded(
                    child: ListView.builder(
                      itemCount: _searchResults.length,
                      itemBuilder: (context, index) {
                        return FlightCard(flight: _searchResults[index]);
                      },
                    ),
                  ),
          ],
        ),
      ),
    );
  }
}

class Flight {
  final String flightNumber;
  final String airline;
  final String departureTime;
  final String arrivalTime;
  final double price;
  final int layovers;

  Flight({
    required this.flightNumber,
    required this.airline,
    required this.departureTime,
    required this.arrivalTime,
    required this.price,
    required this.layovers,
  });
}
