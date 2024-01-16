import axios from 'axios';
const envVariables = require('./env-variables-machine.json');
const { apiIdentifier, auth0Domain, clientId, clientSecret } = envVariables;


let accessToken = null
const redirectUri = 'http://localhost/callback';

const getAccessToken = async () => {
    const options = {
        method: 'POST',
        url: `https://${auth0Domain}/oauth/token`,
        headers: {'content-type': 'application/x-www-form-urlencoded'},
        data: new URLSearchParams({
            grant_type: 'client_credentials',
            client_id: clientId,
            client_secret: clientSecret,
            audience: `https://${auth0Domain}/api/v2/`
        })};
    try {
        const res = await axios.request(options)
        accessToken = res.data.access_token;
    } catch (error) {
        console.error(error);
    }
}

export const updateUserAfterPayment = async (userId: string, subscriptionStatus: string) => {
    if (!accessToken) await getAccessToken();
    const options = {
        method: 'PATCH',
        url: `https://${auth0Domain}/api/v2/users/${userId}`,
        headers: {authorization: `Bearer ${accessToken}`, 'content-type': 'application/json'},
        data: {user_metadata: {subscription_status: subscriptionStatus}}
    };
    try {
        const res = await axios.request(options)
        console.log(res.data);
    } catch(error) {
        console.error(error);
        return "failure"
    }
    return "success"
}