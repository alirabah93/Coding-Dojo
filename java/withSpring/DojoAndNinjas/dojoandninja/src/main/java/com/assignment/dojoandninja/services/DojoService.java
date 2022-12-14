package com.assignment.dojoandninja.services;



import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.assignment.dojoandninja.models.Dojo;
import com.assignment.dojoandninja.repositories.DojoRepository;




@Service
public class DojoService {

	private final DojoRepository dojoRepository;
    
    public DojoService(DojoRepository dojoRepository) {
        this.dojoRepository = dojoRepository;
    }

    public List<Dojo> allDojos() {
        return dojoRepository.findAll();
    }

    public Dojo createDojo(Dojo b) {
        return dojoRepository.save(b);
    }

    public Dojo findDojo(Long id) {
        Optional<Dojo> optionalDojo = dojoRepository.findById(id);
        if(optionalDojo.isPresent()) {
            return optionalDojo.get();
        } else {
            return null;
        }
    }
    
	public Dojo updateDojo(Long id, String name) {
		Dojo dojo = findDojo(id);
	     if(dojo.getId()==id) {
	    	 dojo.setName(name);
	    	 return createDojo(dojo);
	     }
	     else {
	    	 return null;
	     }
	}
	
	public void deleteDojo(Long id) {
		dojoRepository.deleteById(id);
	}
}


