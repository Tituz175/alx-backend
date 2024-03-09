import { createClient } from 'redis';
import { promisify } from "util";

const client = createClient();

client
  .on("error", (err) =>
    console.log(`Redis client not connected to the server: ${err}`)
  )
  .on("connect", () => console.log(`Redis client connected to the server`));

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

const get = promisify(client.get).bind(client)

const displaySchoolValue = async (schoolName) => {
  const response = await get(schoolName).catch((error) => {
    if (error) {
      console.log(error);
      throw error;
    }
  })
  console.log(response);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
