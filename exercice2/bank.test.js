const { getBalance } = require("./bank")
const { retrieveBalance } = require("./bankDAO")


jest.mock('./bankDAO');

describe('Test pour retrieveBalance', () => {
    it('devrait valider que retrieveBalance est appelée', () => {
      
      const accountId='123';
      getBalance(accountId);
        
      
      expect(retrieveBalance).toHaveBeenCalled();
    });

    it('devrait valider que le paremetre accountId est appelée', () => {
       
        const accountId='123';
      getBalance(accountId);
      expect(retrieveBalance).toHaveBeenCalledWith("123");
      });

      // mockretrunvalue
  });
