import '../../styles/globals.css';
 
export default function Design() {
  return (
    <div className="page">
        <div className="center">
          <h2 className="title">Design</h2>

            <h2> Usability </h2>
            <p className="paragraph">
              The idea of SKAPA is to create a tool capable of generating environmental and lifestyle images based on
              an input image or 3D-model. We want to accomplish this as it enables IKEA an ability to adapt their images 
              based on the market which they are meant to be used towards. The main goal of SKAPA is to produce these images 
              in a european environment with focus on living rooms and relaxation areas. However, we believe a tool like 
              this, given enough sample data, would really work for any type of environment. Our goal is to create a very simple
              and straight forward graphical interface so that anyone could use the software regardless of skills in either photography
              or software development. Any images created will be stored in a database which can be accessed by clients IKEA wish
              access to. Temp text.
            </p>

            <h2> Feasibility </h2>
            <p className="paragraph">
              While our AI model in the current state, and most likely later state for the final delivery, is not able to compete with
              other image generators on the market, we still want to give IKEA an idea of what is feasible, especially considering they
              have additional resources. And like we said before, we believe a model like this could extend beyond our current set of 
              environmental parameters. A lot of sample data already exists as we believe IKEA would appreciate if the model could produce 
              similar images to those already found today on their website. Our key takeaway here is it might not be feasible for us to 
              create something like this with our limited sources in terms of funding and time, but it would most definitely be possible 
              for a sizeable company to do so.
            </p>
            
            <h2> Viability </h2>
            <p className="paragraph">
              Based on IKEAs key values and goals we want to tailor SKAPA to be as simple as possible and grant use of the powerful 
              technology we have today. We want to highlight that a tool which is capable of generating images and eliminating the needs 
              of hiring set designers, photographers and the like will likely have a negative impact on job availability among those whose 
              expertise lies within any of these fields. In the end, an image generator would enable cut costs which might aid in reducing 
              prices in their goal to be affordable to anyone.
            </p>

            <h2> About the AI </h2>
            <p className="paragraph">
            In our project generative AI is a cornerstone of our work. Our product is a tool for using generative AI and making it more easy to use for people who are 
            not programmers. We are using a stable diffusion model as our AI model. The main focus in our product is not actually the AI model as it can be replaced 
            by a better model quite easily but rather the user interface and the system of storing generated images to a library for others to use. 
            <br/>
            <br/>
            Our product consists of a graphical user interface that allows users with no programming knowledge to use generative AI to generate product images that are 
            stored in a database 
            for future use and create an image bank of product images for other users to access. The AI in our product is a very swappable part and can be considered the 
            engine in a car, it is very possible to swap the engine in a car and keep using the same car.
            <br/>
            <br/>
            The way our use of AI is implemented is by taking an image of an 
            Ikea product and then taking a so called “masking image” that tells the AI model what it is allowed to change in the image, after that the image is generated 
            using a technology known as diffusion. This results in an image where the product remains intact but the background is changed. 
          </p> 
            
        </div>
      </div>
      

         
  );
}