from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
lostEntries = []
foundEntries = []

class Entry(object):
	def __init__(self, lf, itemname, description, zone, email):
		self.lf = lf
		self.name = itemname
		self.description = description
		self.zone = zone
		self.email = email

class Zone(object):
	def __init__(self, state, city, zipcode):
		self.state = state
		self.city = city
		self.zip = zipcode

@app.route('/lost')
def lostEntries():
	return render_template('losthome.html', lostEntries = lostEntries)

@app.route('/found')
def foundEntries():
	return render_template('foundhome.html', foundEntries = foundEntries)

@app.route('/lostfilter', methods = ["POST"])
def filterLost():
	i = 0
	while i < len(lostEntries):
		if request.form.get("zip") is None:
			if request.form.get("city") is None:
				if lostEntries[i].state != request.form.get("state"):
					lostEntries.remove(lostEntries[i])
			elif lostEntries[i].city != request.form.get("city"):
				lostEntries.remove(lostEntries[i])
		elif lostEntries[i].zip != request.form.get("zip"):
			lostEntries.remove(lostEntries[i])
		else:
			i += 1
	return render_template('lostfilter.html', lostEntries = lostEntries)

@app.route('/foundfilter', methods = ["POST"])
def filterFound():
	i = 0
	while i < len(foundEntries):
		if request.form.get("zip") is None:
			if request.form.get("city") is None:
				if foundEntries[i].state != request.form.get("state"):
					foundEntries.remove(foundEntries[i])
			elif foundEntries[i].city != request.form.get("city"):
				foundEntries.remove(foundEntries[i])
		elif foundEntries[i].zip != request.form.get("zip"):
			foundEntries.remove(foundEntries[i])
		else:
			i += 1
	return render_template('foundfilter.html', foundEntries = foundEntries)

@app.route('/lostentry')
def lostEntry():
	return render_template('lostentry.html')

@app.route('/lostentrysubmission', methods = ["POST"])
def lostEntrySubmission():
	zone = Zone(request.form.get("state"), request.form.get("city"), request.form.get("zip"))
	new = Entry('lost', request.form.get("itemname"), request.form.get("description"), zone, request.form.get("email"))
	lostEntries.append(new)

@app.route('/foundentrysubmission', methods = ["POST"])
def foundEntrySubmission():
	zone = Zone(request.form.get("state"), request.form.get("city"), request.form.get("zip"))
	new = Entry('found', request.form.get("itemname"), request.form.get("description"), zone, request.form.get("email"))
	foundEntries.append(new)

if __name__ == "__main__":
	app.run(debug = True)