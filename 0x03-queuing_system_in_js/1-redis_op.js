import { createClient } from 'redis';

const client = createClient();

client
  .on("error", (err) =>
    console.log(`Redis client not connected to the server: ${err}`)
  )
  .on("connect", () => console.log(`Redis client connected to the server`));

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, (err, reply) => {
    if(err) {
      console.error(err);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

const displaySchoolValue = (schoolName) => {
  console.log(client.GET(schoolName), (err, reply) => {
    if(err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
