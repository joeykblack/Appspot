package project.gwt.package.client.place;

import com.google.gwt.place.shared.PlaceTokenizer;

/**
 * @author joey
 *
 */
public class TemplatePlace extends NamedPlace
{
	
	public TemplatePlace(String name)
	{
		super(name);
	}

	public static class Tokenizer implements PlaceTokenizer<TemplatePlace>
	{

		@Override
		public String getToken(TemplatePlace place)
		{
			return place.getName();
		}

		@Override
		public TemplatePlace getPlace(String token)
		{
			return new TemplatePlace(token);
		}

	}

}
