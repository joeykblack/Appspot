/**
 * 
 */
package project.gwt.package.client.place;

import com.google.gwt.place.shared.Place;

/**
 * @author joeykblack
 *
 */
public class NamedPlace extends Place
{
	
	private String name;
	
	public NamedPlace(String name)
	{
		super();
		this.name = name;
	}

	public String getName()
	{
		return name;
	}

	public void setName(String name)
	{
		this.name = name;
	}

}
