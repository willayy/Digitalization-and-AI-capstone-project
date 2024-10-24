import '../../styles/globals.css';

export default function Study() {
  return (
    <div className="page">
        <div className="center">
        <h2 className="title">Study</h2>
        <div>

          <p className="paragraph">In order to make a product as good as possible, we wanted to interview our imagiend end users to aid our design process to make it as usable as 
            possible. We made an attempt to reach out to People & Culture at Inter IKEA AB but werent able to get a reply within our time frame. Instead, we used
            ChatGPT to make up three different personas of the type of people we would have liked to interview. The three different personas had following jobs:
            Studio Designer, Equipment Technician and Product Stylist and Photogorapher</p>

            <p className="paragraph">We asked the three personas 5 different questions:</p>  
            <ul className="paragraph">
              <li>What do you work with? What is your role?</li>
              <li>Could you describe your workflow? If your workflow changes a lot, describe best and worst case scenarios.</li>
              <li>Could you describe a typical set of pictures? What backgrounds are used?</li>
              <li>What is the most prelavant problem in your workflow? (Regarding product pictures, if applicable)</li>
              <li>Would you appreciate an easy-to-use tool that allows the marketing team to write a prompt and generate a background using AI,
                onto which the product image can be placed, eliminating the need for a physical production set?
              </li>
            </ul>

            <p className="paragraph">
            <b>The Studio Designer</b> plans the set to enable smooth workflow for the technician and photographer on set. They communicate with the client
            to make as good as solution possible given the budget. The types of pictures are usually a mixture of plain backdrop and lifestyle photos.
            Space and budget are usually the two factors constraining the workflow balance. Given the last question, the studio designer had mixed feelings,
            expressing their understanding of the possibilites but were also worried about the need of her knowledge and expertise.
          </p>

          <p className="paragraph">
            <b>The Equipment Technician</b> installs cameras, lightning and similar on the set. The workflow is often great but can falter if something breaks
            or doesnt work as intended. They dont interfer much in regards to the artistic side and let the others decide how the pictures will turn out.
            The technician were positive to the ideas of the tool but emphasized the importance of things looking realisticly.
          </p>

          <p className="paragraph">
            <b>The Product Stylist and Photographer</b> styles the set by making smaller adjustments and captures the photographs. Sometimes they experience
            difficulties in capturing specific products which might have characteristics interfering with light just to name an example. They usually shoot plain 
            backdrops but also more lifestyle and environmental pictures too if that is whats asked for. Besides lightning interference, time management can also
            be an issue. The stylist also thought of the AI-tool to be useful and enables them to focus on the details. They highlighted the importance of everything 
            looking realisticly.
          </p>

          </div>
        </div>
      </div>

      
  );
}
