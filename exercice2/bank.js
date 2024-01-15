const { retrieveBalance } = require('./bankDAO.js') ;

function getBalance(accountId){
    retrieveBalance(accountId);
    
}


module.exports={
    getBalance,
};