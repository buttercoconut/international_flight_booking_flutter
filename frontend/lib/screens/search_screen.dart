import 'package:flutter/material.dart';
import '../widgets/flight_card.dart';
import '../services/api_service.dart';

class SearchScreen extends StatefulWidget {
  @override
  _SearchScreenState createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  List<dynamic> flights = [];
  final _originController = TextEditingController();
  final _destinationController = TextEditingController();

  void _search() async {
    final results = await ApiService.searchFlights(
      _originController.text,
      _destinationController.text,
    );
    setState(() {
      flights = results;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Search Flights')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _originController,
              decoration: InputDecoration(labelText: 'Origin'),
            ),
            TextField(
              controller: _destinationController,
              decoration: InputDecoration(labelText: 'Destination'),
            ),
            SizedBox(height: 16),
            ElevatedButton(onPressed: _search, child: Text('Search')),
            Expanded(
              child: ListView.builder(
                itemCount: flights.length,
                itemBuilder: (context, index) {
                  return FlightCard(flight: flights[index]);
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
