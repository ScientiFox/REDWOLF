//Define the timing variables and set up the clock
let i_time,clock,p_time;
d = new Date();
i_time = d.getTime();
p_time = d.getTime();
clock = 0

//Variables to hold the module selections, especially for checking to allow input submission
module_prev = "";
mod_check = "";
module_sent = false;

//websockets message string
let WSmessage;
WSmessage = "";

//Polling interval for the main update check
setInterval(tickTock,10);

//Open the websocket- 8080 on localhost
sock = new WebSocket('ws://127.0.0.1:8080');

//Attach event handlers for websocket
sock.onopen = function(event){setElement("state","opened");};
sock.onmessage = function(event){onReply(event);}; //The main one to handle connections
sock.onclose = function(event){setElement("state","closed");};

//Flag for if we've talked to the server properly
serverConnected = false;

//Counter for assembling the interaction box scrolling table
let ctr;
ctr = 0;

//Main periodic update function
function tickTock(){
	//Update the timer
	d = new Date();
	clock = d.getTime()-i_time;
	
	//Update the clock display
	document.getElementById('clock').innerHTML="Clocktime: <pre style=\"display: inline;\">"+(clock/1000.0)+"s </pre>";

	//Go looking for a UI update from the server every 1/2 second
	if (d.getTime() - p_time > 500){
		requestUpdate();
		p_time = d.getTime();
	}

	//If the server is talking
	if (serverConnected){
		md = document.getElementById('modulesList').value; //Grab the modulelist selection
		if (md != module_prev){ //If it changed
			sock.send("@S"+md); //Send a setup request for the new module
			module_prev = md; //reset prev-checked flag
		}
	}

	//Check to see if the input button should be available
	c_mod_state = get_mod_state(); //Get the current state of the model selection
	if ((c_mod_state.length != mod_check.length)|(module_prev == "")){ //Basic checks if the module is the same
		module_sent = false; //If not, set sent flag off
		//Update input to tell user to send the module first
		document.getElementById('inpDiv').innerHTML = "<span style=\"color:red;vertical-align: middle;text-shadow: 0px 0px 10px #FAFAFA;\">Send Model First</span>";
	}
	else{ //If not easy check,
		//Loop over all characters in model state
		i = mod_check.length;
		while (i>=0){
			if (mod_check.charAt(i) != c_mod_state.charAt(i)){ //If ever not equal
				i = -2; //pass loop
				module_sent = false; //reset sent flag
				//Update input to tell user to send the module first
				document.getElementById('inpDiv').innerHTML = "<span style=\"color:red;vertical-align: middle;;text-shadow: 0px 0px 10px #FAFAFA\">Send Model First</span>";
			}
			i=i-1; //Keep looping
		}
		//After the loop
		if (i == -1){ //If the whole string is equal
			if (module_sent == false){ //if the module flag hasn't been updated yet
				module_sent = true; //set flag to true
				//Update input to allow submission
				document.getElementById('inpDiv').innerHTML = "<button id=\"inpButton\" onclick=\"inpClick(event);\" style=\"width:8em;\">Send Input</button>";
			}
		}
	}
}

function reset(){
	//Function to reset the UI

	//Fresh date and time
	d = new Date();
	i_time = d.getTime();

	//CLear the warnings and feed boxes, and wipe the interaction block
	document.getElementById('table1').innerHTML = "";
	document.getElementById('warns').innerHTML = "";
	document.getElementById('feed').innerHTML = "";

	//Reset the interaction box table counter, clear WS messages, and prior input
	ctr = 0;
	WSmessage = "";
	inp_prev = null;

	//Reset server and module variables, send a reset request to the server
	serverConnected = false;
	module_prev = '';
	mod_check = "";
	module_sent = false;
	sock.send("@R");

}

function requestUpdate(){
	//Send a request for updates from the server
	sock.send("@U")
	}

function onReply(event){
	// Primary function for handling messages from the server

	//Get the actual message data
	WSmessage=event.data;

	// If a panel message
	if (WSmessage.charAt(0) == "P"){
		//Grab the substring of the panel HTML which is the content of the message, and insert into the panel div
		document.getElementById('panel').innerHTML = WSmessage.substring(1,WSmessage.length);
		module_sent = false; //reset the sent module flag
		document.getElementById('inpDiv').innerHTML = "<span style=\"color:red;\">Send Model First</span>"; //update input submit
	}
	//If a feed message
	else if (WSmessage.charAt(0) == "F"){
		//Put message contents into the feed box
		document.getElementById('feed').innerHTML = WSmessage.substring(1,WSmessage.length)+ "<br>" + document.getElementById('feed').innerHTML;
	}
	//If an output message
	else if (WSmessage.charAt(0) == "O"){
		lab = "msgbox"+ctr; //Construct the current tabel row div ID
		//Insert the message contents into that div
		document.getElementById(lab).innerHTML = WSmessage.substring(1,WSmessage.length);
	}
	//If a warning message
	else if (WSmessage.charAt(0) == "W"){
		//Put message contents into warning box
		document.getElementById('warns').innerHTML = WSmessage.substring(1,WSmessage.length);
	}
	//If an input message
	else if (WSmessage.charAt(0) == "I"){
		//Add a table line for the new input
		addTableLine(WSmessage.substring(1,WSmessage.length));
	}
	//If a setup message
	else if (WSmessage.charAt(0) == "S"){
		serverConnected = true; //Note we are defintiely connected to the server now
		module_sent = false; //Clear module sent flag
		module_prev = ""; //wipe prev module
		mod_check = ""; //no module check text
		document.getElementById('inpDiv').innerHTML = "<span style=\"color:red;\">Send Model First</span>"; //reset input HTML
		document.getElementById("ModuleSel").innerHTML = WSmessage.substring(1,WSmessage.length); //Populate module select with message contents
	}
}

function pass(){}//donothing

function get_mod_state(){
	//Function to check the current module select state- for controlling valid input submission state

	//Grab the panel HTML
	inpCard  = document.getElementById('panel');
	if (document.getElementById('moduleName')){ //If there's a name there by now
		nme = document.getElementById('moduleName').innerHTML; //Grab it
	}
	else{nme="";} //Else, currently blank

	//Get selection options in the input panel
	sels = inpCard.getElementsByTagName('select');

	//Loop over the elements and build a state string with the name and select box ids and values
	let i = 0;
	let op = ""+"name§"+nme+"§"; //Add in the name string
	while (i<sels.length){ //Add in each select type and contents
		op = op + sels[i].id;
		op = op + "§";
		op = op + sels[i].value;
		op = op + "§";
		i = i + 1;
	}
	
	//Add in the system command value, too
	op = op + document.getElementById('addlSYS').value; 

	return op //Return the ID string
}

function inpClick(event){
	//Function to process a click for the buttons

	//If the module button is pressed
	if (event.target.id == "modButton"){

		inpCard  = document.getElementById('panel'); //Get the panel id element
		nme = document.getElementById('moduleName').innerHTML; //Grab the name of the module
		inps = inpCard.getElementsByTagName('input'); //Get the inputs
		sels = inpCard.getElementsByTagName('select'); //Get the selects

		//Looping over all the select boxes
		let i = 0;
		let op = ""+"name§"+nme+"§"; //Start the output with the name
		while (i<sels.length){ //add the id and value of each select to the output
			op = op + sels[i].id;
			op = op + "§";
			op = op + sels[i].value;
			op = op + "§";
			i = i + 1;
		}
		i = 0; //Looping over all the inputs
		while (i < inps.length){ //add the id and value of each input to the output
			op = op + inps[i].id;
			op = op + "§";
			op = op + inps[i].value;
			op = op + "§";
			i = i + 1;
		}

		//Add the system message input to the output
		op = op + "SYSTEM§" + document.getElementById('addlSYS').value;
		sock.send("@M"+op); //Send the output as a module message
		module_sent = true; //note that the module has been sent
		mod_check = get_mod_state(); //Get a fresh module state and update the input button
		document.getElementById('inpDiv').innerHTML = "<button id=\"inpButton\" onclick=\"inpClick(event);\" style=\"width:8em;\">Send Input</button>";
	}

	//If the input button is pressed
	if (event.target.id == "inpButton"){

		//Get the input card element
		inpCard  = document.getElementById('panel');
		nme = document.getElementById('moduleName').innerHTML; //Grab the module name
		inps = inpCard.getElementsByTagName('input'); //Grab the input elements list

		//Looping over all the input elements
		let i = 0;
		let op = ""+"name§"+nme+"§"; //Start the output with the module name
		while (i < inps.length){ //For each input, add the id and name to the output
			op = op + inps[i].id;
			op = op + "§";
			op = op + inps[i].value;
			op = op + "§";
			i = i + 1;
		}

		//Add the system command to the output
		op = op + "SYSTEM§" + document.getElementById('addlSYS').value;

		//Send the output as an input message
		sock.send("@I"+op);
	}

}


function addTableLine(inp){
	//Function to extend the table in the interaction block using ctr

	ctr = ctr + 1; //Increment the counter to the next row

	inHTML = document.getElementById('table1').innerHTML; //Get the innerHTML of the table itself

	//Construct a new line with the input inserted into column one of the table with an id of msgbox+ctr,followed by the previous table rows
	inHTML =
	"<tr><td class=\"t1\">" +inp+ "</td>"
	+ "<td class=\"t2\"> <span id=\"msgbox"+ctr+"\" class=\"tbox\">" + " " + "</span></td>"+"</tr>"
	+ inHTML;
	document.getElementById('table1').innerHTML = inHTML; //Set the new table value into the table div
}


